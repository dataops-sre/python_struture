from jobs.classes.basic import Basic

class Job1(Basic):
    """docstring for Job1"""
    def __init__(self):
        super(Job1, self).__init__()
    
    def abstractcall(self):
        print("I am job1")

if __name__=='__main__':
    job = Job1()
    job.run()