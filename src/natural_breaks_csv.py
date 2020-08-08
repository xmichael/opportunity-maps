#!/usr/bin/env python3
# coding: utf-8
"""
Functions for adding Natural Breaks (Jenks) classification score on existing CSV files
"""

import pandas as pd
import jenkspy
import matplotlib.pyplot as plt


class NaturalBreaksCSV(object):
    """Add an extra attribute to a CSV file with a Jenks score for one of its properties.
    """

    @property
    def raw_values(self) -> []:
        """
        Return the the original scores as a sorted python array. Useful for plotting.
        """
        if self.result is None:
            return None
        return self.result.sort_values([self.field_name])[self.field_name].values

    def __init__(self, input_file: str, output_file: str, field_name: str, nclass: int):
        super(NaturalBreaksCSV, self).__init__()
        self.input_file = input_file
        self.output_file = output_file
        self.field_name = field_name
        self.nclass = nclass

        self.breaks = None
        self.result = None

    def visualise_jenks(self) -> bool:
        """
        Visualises the classified scores. Useful for evaluating the 
        effectiveness of the classification.
        """
        if self.breaks is None:
            return False
        # show breaks as dashed lines
        for line in self.breaks:
            plt.plot([line for _ in range(len(self.raw_values))], "k--")
        plt.plot(self.raw_values)
        plt.show()
        plt.close()

    def classify_csv(self) -> None:

        df = pd.read_csv(self.input_file)
        breaks = jenkspy.jenks_breaks(df[self.field_name], nb_class=self.nclass)

        # Use [ 1, 2, 3 ... , nclass ] as scores for each bin
        labels = [i for i in range(1, self.nclass + 1)]

        df["JENKS_BIN"] = pd.cut(
            df[self.field_name], bins=breaks, labels=labels, include_lowest=True
        )
        df_sorted = df.sort_values("JENKS_BIN")

        self.breaks = breaks
        self.result = df_sorted

    def save_to_csv(self) -> None:
        self.result.to_csv(self.output_file, index=False)


def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        description="Classify CSV file using Natural Breaks (Jenks) algorithm."
    )

    parser.add_argument("input_file", help="input CSV file")
    parser.add_argument("output_file", help="input CSV file")
    parser.add_argument("field_name", help='field name of the CSV file. e.g. "SCORE"')
    parser.add_argument(
        "-n", type=int, default=10, help="number of classes (default: 10)"
    )
    parser.add_argument(
        "--plot",
        default=False,
        action="store_true",
        help="plot classification result (default: False)",
    )
    args = parser.parse_args()
    return args


def test():
    cl = NaturalBreaksCSV(
        "./tests/data/carbon_test_100.csv", "./tests/out.csv", "SCORE", 10
    )
    (df, breaks) = cl.classify_csv()
    cl.visualise_jenks()


def main():
    args = parse_arguments()

    cl = NaturalBreaksCSV(args.input_file, args.output_file, args.field_name, args.n)
    cl.classify_csv()
    if args.plot:
        cl.visualise_jenks()
    print(cl.result)
    cl.save_to_csv()


if __name__ == "__main__":
    main()
