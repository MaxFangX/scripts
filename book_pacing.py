

def main(pages, days):
    """
    Returns the reading plan of the book
    """
    pages, days = int(pages), int(days)
    pages_per_day = pages // days + 1
    for i in range(days):
        end_page = pages if i == days - 1 else pages_per_day * (i + 1)
        print "Day {}: Page {} to {}".format(i + 1, pages_per_day * i + 1, end_page)


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print "Need command line args:"
        print "python book_pacing.py [# of pages in book] [# number of days to read]"
    else:
        print "\nPlan for splitting book with {} pages into {} days:\n".format(sys.argv[1], sys.argv[2])
        main(sys.argv[1], sys.argv[2])
        print ""
