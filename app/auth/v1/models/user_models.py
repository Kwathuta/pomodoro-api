class UserModels:
    """
    Class for the user operations
    """

    users = []

    def __init__(self, username, task, task_timer, break_timer, task_completed):
        """
        Initialize the user models
        """
        self.id = len(UserModels.users) + 1
        self.username = username
        self.task = task
        self.task_timer = task_timer
        self.break_timer = break_timer
        self.task_completed = task_completed

    def save_user(self):
        """
        Method to register user instance and update the data structure
        """
        user_record = dict(
            id=self.id,
            username=self.username,
            task=self.task,
            task_timer=self.task_timer,
            break_timer=self.break_timer,
            task_completed=self.task_completed
        )
        self.users.append(user_record)
