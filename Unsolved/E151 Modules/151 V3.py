"""
This module solves Euler 151 - 'Paper Sheets of Standard Sizes.
The intent of this module was to implement a solution using classes (i.e. for practice).
'"""
# PROBLEM:
#
# A printing shop runs 16 batches (jobs) every week and each batch requires a sheet of special
# colour-proofing paper of  size A5.
#
# Every Monday morning, the foreman opens a new envelope, containing a large sheet of the special
# paper with size A1.
#
# He proceeds to cut it in half, thus getting two sheets of size A2.
# Then he cuts one of them in half to get two sheets of size A3 and so on until he obtains
# the A5-size sheet needed for the first batch of the week.
#
# All the unused sheets are placed back in the envelope.
# At the beginning of each subsequent batch, he takes from the envelope one sheet of paper at random.
# If it is of size A5, he uses it. If it is larger, he repeats the 'cut-in-half' procedure until he
# has what he needs and any remaining sheets are always placed back in the envelope.
#
# Excluding the first and last batch of the week, find the expected number of times (during each week) that
# the foreman finds a single sheet of paper in the envelope.
#
# Give your answer rounded to six decimal places using the format x.xxxxxx .


class PrintShopBag(object):

    """Captures an instance of the printer's bag.

    The number of sheets of each paper size is tracked as an attribute.
    P captures the probability that a given bag state is the outcome of its predecessor state.
    Batch represents the batch number of a bag state in a given week.
    """

    A1 = 0
    A2 = 0
    A3 = 0
    A4 = 0
    A5 = 0
    Last_Batch = []
    P = 0.0
    Batch = 0
    Choices = A1 + A2 + A3 + A4 + A5
    Zero_Count = 0
    Total_Count = 0

    def __init__(self, A1=1, A2=0, A3=0,
                 A4=0, A5=0, P=1, Batch=0,
                 Choices=1, Last_Batch=[],
                 Zero_Count=0, Total_Count=0):

        """Initializes bag to first batch if quantities are not provided."""

        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.A5 = A5
        self.P = P
        self.Batch = Batch
        self.Choices = Choices
        self.Last_Batch = Last_Batch
        self.Zero_Count = Zero_Count
        self.Total_Count = Total_Count


    def Take_A1(self):

        """Removes an A1; adds one A2-A5."""

        self.A1 -= 1
        self.A2 += 1
        self.A3 += 1
        self.A4 += 1
        self.A5 += 1


    def Take_A2(self):

        """Removes an A2; adds one A3-A5."""

        self.A2 -= 1
        self.A3 += 1
        self.A4 += 1
        self.A5 += 1


    def Take_A3(self):

        """Removes an A3; adds one A4-A5."""

        self.A3 -= 1
        self.A4 += 1
        self.A5 += 1


    def Take_A4(self):

        """Removes an A4; adds one A5."""

        self.A4 -= 1
        self.A5 += 1


    def Take_A5(self):

        """Removes an A5."""

        self.A5 -= 1


    def Run_Batch(self):

        """"Advances the bag state by one round.  Stores last bag state."""

        if self.Batch == 0:
            self.Last_Batch.append([0, 1, 1, 1, 1, 1.0])
        if self.Batch > 0:

# Abandoning this implementation.

