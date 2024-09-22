from datetime import datetime

def format_date(date_string):
    """Format date string for display."""
    try:
        # Parse the date string into a datetime object
        date_object = datetime.strptime(date_string, "%Y-%m-%d")
        
        #  this Formats the date object into a more readable format
        formatted_date = date_object.strftime("%B %d, %Y")  
        return formatted_date
    except ValueError as e:
        return f"Error: {e} - Please provide a date in 'YYYY-MM-DD' format."