from craigslist import CraigslistGigs, CraigslistJobs

cl_g = CraigslistGigs(category='cpg')

for result in cl_g.get_results(sort_by='newest', geotagged=True):
    print(result)