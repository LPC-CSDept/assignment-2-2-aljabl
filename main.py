def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    #assign value to celcius variable
    celcius = int(input('What\'s the temperature in Celcius? '))

    #conversion form Celcius to Fahrenheit 
    fahrenheit = celcius * 1.8 + 32

    #print converted value 
    print(f'Fahrenheit:  {fahrenheit:.2f}')

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
