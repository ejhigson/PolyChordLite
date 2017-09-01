import os

class PolyChordSettings:
    """
    PolyChord settings

    For full details of nested sampling and PolyChord, please refer to:

    Parameters
    ----------
    nDims: int
        Dimensionality of the model, i.e. the number of physical parameters.

    nDerived: int
        The number of derived parameters (can be 0).


    Keyword arguments
    -----------------
    nlive: int
        (Default: nDims*25)
        The number of live points.
        Increasing nlive increases the accuracy of posteriors and evidences,
        and proportionally increases runtime ~ O(nlive).

    num_repeats : int
        (Default: nDims*5)
        The number of slice slice-sampling steps to generate a new point.
        Increasing num_repeats increases the reliability of the algorithm.
        Typically
        * for reliable evidences need num_repeats ~ O(5*nDims).
        * for reliable posteriors need num_repeats ~ O(nDims)

    do_clustering : boolean
        (Default: True)
        Whether or not to use clustering at run time.

    feedback : {0,1,2,3}
        (Default: 1)
        How much command line feedback to give

    precision_criterion : float
        (Default: 0.001)
        Termination criterion. Nested sampling terminates when the evidence
        contained in the live points is precision_criterion fraction of the
        total evidence.

    max_ndead : int
        (Default: -1)
        Alternative termination criterion. Stop after max_ndead iterations.
        Set negative to ignore (default).

    boost_posterior : float
        (Default: 0.0)
        Increase the number of posterior samples produced.  This can be set
        arbitrarily high, but you won't be able to boost by more than
        num_repeats
        Warning: in high dimensions PolyChord produces _a lot_ of posterior
        samples. You probably don't need to change this

    posteriors : boolean
        (Default: True)
        Produce (weighted) posterior samples. Stored in <root>.txt.

    equals : boolean
        (Default: True)
        Produce (equally weighted) posterior samples. Stored in
        <root>_equal_weights.txt

    cluster_posteriors : boolean
        (Default: True)
        Produce posterior files for each cluster?
        Does nothing if do_clustering=False.

    write_resume : boolean
        (Default: True)
        Create a resume file.

    read_resume : boolean
        (Default: True)
        Read from resume file.

    write_stats : boolean
        (Default: True)
        Write an evidence statistics file.

    write_live : boolean
        (Default: True)
        Write a live points file.

    write_dead : boolean
        (Default: True)
        Write a dead points file.

    update_files : int
        (Default: nlive)
        How often to update the files in <base_dir>.

    base_dir : string
        (Default: 'chains')
        Where to store output files.

    file_root : string
        (Default: 'test')
        Root name of the files produced.

    grade_frac : List[float]
        (Default: 1)
        The amount of time to spend in each speed.

    grade_dims : List[int]
        (Default: 1)
        The number of parameters within each speed.
    """
    def __init__(self, nDims, nDerived, **kwargs):

        self.nlive = nDims * 25
        self.nlive = kwargs.pop('nlive', nDims*25)
        self.num_repeats = kwargs.pop('num_repeats', nDims*5)
        self.do_clustering = kwargs.pop('do_clustering', True)
        self.feedback = kwargs.pop('feedback', 1)
        self.precision_criterion = kwargs.pop('precision_criterion', 0.001)
        self.max_ndead = kwargs.pop('max_ndead', -1)
        self.boost_posterior = kwargs.pop('boost_posterior', 0.0)
        self.posteriors = kwargs.pop('posteriors', True)
        self.equals = kwargs.pop('equals', True)
        self.cluster_posteriors = kwargs.pop('cluster_posteriors', True)
        self.write_resume = kwargs.pop('write_resume', True)
        self.write_paramnames = kwargs.pop('write_paramnames', False)
        self.read_resume = kwargs.pop('read_resume', True)
        self.write_stats = kwargs.pop('write_stats', True)
        self.write_live = kwargs.pop('write_live', True)
        self.write_dead = kwargs.pop('write_dead', True)
        self.update_files = kwargs.pop('update_files', self.nlive)
        self.base_dir = kwargs.pop('base_dir', 'chains')
        self.file_root = kwargs.pop('file_root', 'test')
        self.grade_dims = kwargs.pop('grade_dims', [nDims])
        self.grade_frac = kwargs.pop('grade_frac', [1.0]*len(self.grade_dims))

        if kwargs:
            raise TypeError('Unexpected **kwargs in Contours constructor: %r' % kwargs)

        if len(self.grade_frac) != len(self.grade_dims):
            raise ValueError('grade_dims and grade_frac must be the same length')

        if sum(self.grade_dims) != nDims:
            raise ValueError('grade_dims must sum to the total dimensionality: sum(' + str(self.grade_dims) + ') /= %i' % nDims)

    @property
    def cluster_dir(self):
        return os.path.join(self.base_dir,'clusters')

