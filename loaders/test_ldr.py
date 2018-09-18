def main():

    src = open('/Users/greggmidon/data/job/PS_PERSON_NAME.txt', 'r')
    #src = open('/Users/greggmidon/data/job/test_names.txt', 'r')

    dest = open('/Users/greggmidon/data/job/testout.txt', 'a')

    i = 0
    max = 200

    try:

        for line in src:

            i += 1
            #line = line[:-1]
            #fields = line.split('|')


            if i > start and i < end:
                dest.write(line + '\n')


    except Exception:
        print('Error: ' + str(i) + ', ' + line)

    src.close()
    dest.close()


if __name__ == '__main__':

    main()
