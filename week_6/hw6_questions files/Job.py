from functools import total_ordering


@total_ordering
class Job:
    last_job_id = 0

    def __init__(self, job_description, job_rank,
                 job_request_resources):
        if not isinstance(job_description, str):
            raise TypeError("job_description should be string.")
        if not isinstance(job_rank, int):
            raise TypeError("job_rank should be int.")
        if not job_rank > 0:
            raise ValueError("job_rank should be greater then 0.")
        if not isinstance(job_request_resources, int):
            raise TypeError("job_request_resources should be int.")
        if not job_request_resources > 0:
            raise ValueError("job_request_resources should be greater then 0.")
        self.__job_id = Job.last_job_id
        Job.last_job_id += 1
        self.__description = job_description
        self.__rank = job_rank
        self.__job_requested_resources = job_request_resources

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
        return f"ID: {self.__job_id}, Rank: {self.__rank}, Resources: {self.__job_requested_resources}"

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass


job_1 = Job(job_description="first job example", job_rank=1, job_request_resources=2)
job_2 = Job(job_description="another job example", job_rank=10, job_request_resources=5)
job_3 = Job(job_description="third example", job_rank=5, job_request_resources=1)
job_list = [job_1, job_2, job_3]
for item in job_list:
    print(item)
for job in job_list:
    print(f"Current Job ID: {job.get_id()}")
    print(f" requested resources before updates: {job.get_job_requested_resources()}")
    job.set_job_requested_resources(3)
    print(f" requested resources after updates: {job.get_job_requested_resources()}")
