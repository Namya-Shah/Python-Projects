date = int(input("Enter a year (or enter 0 if you want to see the ): "))

president_dict = {1: "Rajendra Prasad",
                  2: "Sarvepalli Radhakrishnan",
                  3: "Zakir Hussain",
                  4: "V.V.Giri",
                  5: "Mohammad Hidayatullah",
                  6: "Fakhruddin Ali Ahmed",
                  7: "B.D. Jatti",
                  8: "Neelam Sanjiva Reddy",
                  9: "Zail Singh",
                  10: "Ramaswamy Venkataraman",
                  11: "Shankar Dayal Sharma",
                  12: "K. R. Narayan",
                  13: "A.P.J. Abdul Kalam",
                  14: "Pratibha Patil",
                  15: "Pranab Mukherjee",
                  16: "Ramnath Kovind",
                  17: "Droupadi Murmu"}

pm_dict = {
    1: "Jawaharlal Nehru",
    2: "Gulzarilal Nanda",
    3: "Lal Bahadur Shastri",
    4: "Indira Gandhi",
    5: "Morarji Desai",
    6: "Charan Singh",
    7: "Rajiv Gandhi",
    8: "Vishwanath Pratap Singh",
    9: "Chandra Shekhar",
    10: "P.V. Narsimha Rao",
    11: "Atal Bihari Vajpayee",
    12: "H.D. Deve Gowda",
    13: "Inder Kumar Gujral",
    14: "Manmohan Singh",
    15: "Narendra Modi"
}

def president():
    if date >= 1950 and date < 1962:
        print("First president was", president_dict[1] + ".")
    elif date >= 1962 and date < 1967:
        print("Second president was", president_dict[2] + ".")
    elif date >= 1967 and date < 1969:
        print("Third president was", president_dict[3] + ".")
    elif date >= 1969 and date < 1974:
        print("There were 3 presidents on different term period")
        print("Fourth president for term '3 May 1969' to '20 July 1969' was", president_dict[4] + ".")
        print("Fourth president for term '20 July 1969' to '23 August 1969' was", president_dict[5] + ".")
        print("First president was", president_dict[4] + ".")
    elif date >= 1974 and date < 1977:
        print("Fifth president was", president_dict[6] + ".")
    elif date >= 1977 and date < 1982:
        print("There were 2 presidents in this year")
        print("Sixth president in term '12 February 1977' to '24 July 1977' was", president_dict[7] + ".")
        print("Sixth president was", president_dict[8] + ".")
    elif date >= 1982 and date < 1987:
        print("There were 2 presidents in this time period")
        print("Seventh president '6 October 1982' to '31 October 1982' was", president_dict[5] + ".")
        print("Seventh president was", president_dict[9] + ".")
    elif date >= 1987 and date < 1992:
        print("Eigth president was", president_dict[10] + ".")
    elif date >= 1992 and date < 1997:
        print("Nineth president was", president_dict[11] + ".")
    elif date >= 1997 and date < 2002:
        print("Tenth president was", president_dict[12] + ".")
    elif date >= 2002 and date < 2007:
        print("Eleventh president was", president_dict[13] + ".")
    elif date >= 2007 and date < 2012:
        print("Twelveth president was", president_dict[14] + ".")
    elif date >= 2012 and date < 2017:
        print("Thirteenth president was", president_dict[15] + ".")
    elif date >= 2017 and date < 2022:
        print("Fourteenth president was", president_dict[16] + ".")
    elif date >=2022 and date < 2027:
        print("Fifteenth president is", president_dict[17] + ".")

def prime_minister():
    if date >= 1947 and date < 1964:
        print("First prime minister was", pm_dict[1])
    elif date >= 1964 and date < 1966:
        print("There were two prime minister among this term period")
        print("Second prime minister from '27 May 1964' to '9 June 1964' was", pm_dict[2])
        print("Second prime minster was", pm_dict[3])
    elif date >= 1966 and date < 1977:
        print("There were two prime minister among this term period")
        print("Third prime minister from '11 January 1966' to '24 January 1966' was", pm_dict[2])
        print("Third prime minister was", pm_dict[4])
    elif date >= 1977 and date < 1979:
        print("Fourth prime minister was", pm_dict[5])
    elif date >= 1979 and date < 1980:
        print("Fifth prime minister was", pm_dict[6])
    elif date >= 1980 and date < 1984:
        print("Sixth prime minister was", pm_dict[4])
    elif date >= 1984 and date < 1989:
        print("Seventh prime minister was", pm_dict[7])
    elif date >= 1989 and date < 1990:
        print("Eigth prime minister was", pm_dict[8])
    elif date >= 1990 and date < 1991:
        print("Nineth prime minister was", pm_dict[9])
    elif date >= 1991 and date < 1996:
        print("Tenth prime minister was", pm_dict[10])
    elif date >= 1996 and date < 1997:
        print("Eleventh prime minister for '13 days' was", pm_dict[11])
        print("Eleventh prime minister was", pm_dict[12])
    elif date >= 1997 and date < 1998:
        print("Twelveth prime minister was", pm_dict[13])
    elif date >= 1998 and date < 2004:
        print("Thirteenth prime minister was", pm_dict[11])
    elif date >= 2004 and date < 2014:
        print("Fourteenth prime minister was", pm_dict[14])
    elif date >= 2014 and date < 2022:
        print("Fifteenth prime minister is", pm_dict[15])
    

    

print("1. President")
print("2. Prime Minister")
print("3. Chief Minister")
choice = int(input("Enter a choice: "))
if choice == 1:
    president()
elif choice == 2:
    prime_minister()
elif choice == 3:
    pass