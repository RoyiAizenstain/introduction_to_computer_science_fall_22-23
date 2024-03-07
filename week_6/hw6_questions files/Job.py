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
        return self.__rank

    def get_description(self):
        return self.__description

    def get_id(self):
        return self.__job_id

    def set_description(self, new_description):
        if not isinstance(new_description, str):
            raise TypeError("new_description should be string.")
        self.__description = new_description

    def set_rank(self, new_rank):
        if not isinstance(new_rank, int):
            raise TypeError("new_rank should be int.")
        if not new_rank > 0:
            raise ValueError("new_rank should be greater then 0.")
        self.__rank = new_rank

    def set_job_requested_resources(self, new_job_requested_resources):
        if not isinstance(new_job_requested_resources, int):
            raise TypeError("job_request_resources should be int.")
        if not new_job_requested_resources > 0:
            raise ValueError("job_request_resources should be greater then 0.")
        self.__job_requested_resources = new_job_requested_resources

    def get_job_requested_resources(self):
        return self.__job_requested_resources

    def __repr__(self):
        return f"ID: {self.__job_id}, Rank: {self.__rank}, Resources: {self.__job_requested_resources}"

    def __eq__(self, other):
        return self.__rank == other.__rank

    def __lt__(self, other):
        return self.__rank < other.__rank
