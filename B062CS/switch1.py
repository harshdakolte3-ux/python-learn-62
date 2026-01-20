def main(i):
            switcher={
                0:'sunday',
                1:'Monday',
                2:'Tuesday',
                3:'Wednesday',
                4:'Thursday',
                5:'Friday',
                6:'saturday',

            }

            return switcher.get(i,"Invalid day of week")
            print(week(6))

if __name__ == "__main__":
    main()