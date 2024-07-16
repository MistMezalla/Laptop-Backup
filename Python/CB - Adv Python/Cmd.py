import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-P","--Physics",help="Marks in Physics")
    parser.add_argument("-C", "--Chemistry", help="Marks in Chemistry")
    parser.add_argument("-M", "--Maths", help="Marks in Maths")
    parser.add_argument("-op","--Operation",help="Operation to be preformed on marks",choices=["Average"])

    args = parser.parse_args()

    res = None

    np=int(args.Physics)
    nc=int(args.Chemistry)
    nm=int(args.Maths)

    print(f"{(np+nc+nm)/3:.2f}")


