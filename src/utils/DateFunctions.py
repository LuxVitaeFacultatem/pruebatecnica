from datetime import datetime

class Date:
    @classmethod
    def get_date(self):
        actual_date = datetime.now()
        formatted_date = actual_date.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_date
    
    @classmethod
    def time_Calculate(self, start_date, end_date):
        format = "%Y-%m-%d %H:%M:%S"
        
        # Convert the date strings to datetime objects
        start_date_dt = datetime.strptime(start_date, format)
        end_date_dt = datetime.strptime(end_date, format)
        
        # Calculate the difference in minutes
        difference = end_date_dt - start_date_dt
        elapsed_minutes = int(difference.total_seconds() / 60)
        
        return elapsed_minutes

    
    @classmethod
    def convert_date(self, date):
        return datetime.strftime(date, "%Y-%m-%d %H:%M:%S")
