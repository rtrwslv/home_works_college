def diary(records, start_date):
    """Function makes file with pirate diary, using given arguments"""
    file = open("diary", "w")
    for i in range(len(records)):
        file.write(
            str(
                (
                    datetime.strptime(start_date, "%d-%m-%Y") + timedelta(days=i)
                ).strftime("%d-%m-%Y")
            )
            + " "
            + str(records[i])
            + "\n"
        )

