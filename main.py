def calculator():
    while True:
        print("\nCalculator")

        a = input("\nEnter the First number to calculate: ")
        b = input("Enter the Second number: ")

        print("Choose\n")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")

        # Convert input to integer
        option = int(input("Enter the option (1/2/3/4/5): "))

        if option == 1:
            # Convert inputs to floats and calculate sum
            sum = float(a) + float(b)

            result = sum
            print("\nAnswer = ", result)

        elif option == 2:

            subtract = float(a) - float(b)
            result = subtract
            print("\nAnswer = ", result)

        elif option == 3:

            multiply = float(a) * float(b)

            result = multiply

            print("\nAnswer = ", result)


        elif option == 4:
            divide = float(a) / float(b)
            result = divide
            print("\nAnswer = ", result)

        elif option == 5:

            remainder = float(a) % float(b)
            result = remainder
            print("\nAnswer = ", result)


calculator()