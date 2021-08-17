from jobs.classes.basic import Basic

class Job2(Basic):
    """docstring for Job1"""
    def __init__(self):
        super(Job2, self).__init__()
    
    def abstractcall(self):
        print("I am job2")

if __name__=='__main__':
   	job = Job2()
   	job.run()
