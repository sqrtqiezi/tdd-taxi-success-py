import argparse
from taxi import process_file

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-data",
                        type=str,
                        required=True,
                        metavar="./resource/testData.txt",
                        help="test data path")
    args = parser.parse_args()
    test_data_file = args.test_data
    receipt = process_file(test_data_file)
    print(receipt)
