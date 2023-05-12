def Date_Calculate(y ,m, d):

    import datetime  # importing datetime module
    today = datetime.datetime.now().date()
    d_o_b = datetime.date(y, m, d)  
    
    age = int((today - d_o_b).days/365)
    print(age, f'years')
    
Date_Calculate(2001, 3, 12)

