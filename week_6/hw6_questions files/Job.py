
from functools import total_ordering
@total_ordering
class Job:
    
    def __init__(self, job_description, job_rank,
                 job_request_resources):
        pass

    def get_rank(self):
        pass

    def get_description(self):
        pass

    def get_id(self):
        pass

    def set_description(self, new_description):
        pass

    def set_rank(self, new_rank):
        pass

    def set_job_requested_resources(self, new_job_requested_resources):
        pass

    def get_job_requested_resources(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass
