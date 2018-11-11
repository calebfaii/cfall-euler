# The RSA encryption is based on the following procedure:

# Generate two distinct primes p and q.
# Compute n=pq and phi=(p-1)(q-1).
# Find an integer e, 1<e<phi, such that gcd(e,phi)=1.

# A message in this system is a number in the interval [0,n-1].
# A text to be encrypted is then somehow converted to messages (numbers
# in the interval [0,n-1]).

# To encrypt the text, for each message, m, c=m**e mod n is calculated.

# To decrypt the text, the following procedure is needed: calculate d such
# that ed=1 mod phi, then
# for each encrypted message, c, calculate m=c**d mod n.

# There exist values of e and m such that m**e mod n == m.
# We call messages m for which me mod n == m unconcealed messages.
#
# An issue when choosing e is that there should not be too many unconcealed messages.
# For instance, let p=19 and q=37.
# Then n=19*37=703 and phi=18*36=648.
# If we choose e=181, then, although gcd(181,648)=1 it turns out that all
# possible messages
# m (0<=m<=n-1) are unconcealed when calculating m**e mod n.

# For any valid choice of e there exist some unconcealed messages.
# It's important that the number of unconcealed messages is at a minimum.

# Choose p=1009 and q=3643.
# Find the sum of all values of e, 1<e<phi(1009,3643) and gcd(e,phi)=1, so
# that the number of
# unconcealed messages for this value of e is at a minimum.

import progressbar
import fractions


class MessageHelper(object):

    """
    This class contains all "given" constants as well as a handful of derived values.

    Methods for computing and comparing common factors are also included.
    """

    def __init__(self, p, q):

        """
        Upon instantiation, a given p and q are used to compute n and phi.
        """

        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = None
        self.e_candidates = []

    def set_e(self, e):

        """
        Sets e without direct attribute access, because I am a conscientious programmer.
        """

        self.e = e

    @classmethod
    def get_factors(cls, n):

        """
        Receives a number as argument; returns the distinct factors of that number.
        """

        return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))

    @staticmethod
    def check_gcd(a, b):

        """
        If the GCD of two numbers a and b is 1, returns True; else False.
        """

        a_factors = set(i for i in MessageHelper.get_factors(a))
        b_factors = set(i for i in MessageHelper.get_factors(b))
        intersection = a_factors.intersection(b_factors)
        gcd_is_one = False

        if intersection == {1}:
            gcd_is_one = True
        return gcd_is_one

    def get_all_e(self):

        """
        Generates a list of candidate values for e.  Excludes arbitrarily small common factors of e and n.
        """

        excluded_factors = [2, 3, 4, 6, 7, 8, 9]
        bar = progressbar.ProgressBar(1, self.phi)

        for num in xrange(1, self.phi, 2):
            bad_e = False

            for factor in excluded_factors:
                if num % factor == 0:
                    bad_e = True

            if not bad_e:
                if self.check_gcd(num, self.phi):
                    self.e_candidates.append(num)
            bar.update(num)

    def encrypt(self, m):

        """
        Receives an unencrypted message, m, and returns an encrypted message, c.
        """

        c = (m ** self.e) % self.n
        return c

    def decrypt(self, c):

        """
        Receives an encrypted message, c, and returns an unencrypted message, m.
        """

        ed = 1 % self.phi
        d = ed / self.e
        m = (c ** d) % self.n
        return m

    def is_unconcealed(self, m):

        """
        Returns True if the message is unconcealed; else False.
        """

        if (m ** self.e) % self.n == m:
            return True
        else:
            return False


def solve():

    """
    For a given p and q, this function evaluates all potential candidates of e.

    The objective is to find values of e for which the total number of unconcealed
    messages is minimized.
    """

    msg = MessageHelper(1009, 3643)
    msg.get_all_e()
    print "There are %d candidates of e." % len(msg.e_candidates)

    results = {}

    bar = progressbar.ProgressBar(1, len(msg.e_candidates) + 1)
    num = 1
    for candidate in msg.e_candidates:
        msg.set_e(candidate)
        count_unconcealed = 0
        for m in range(1, msg.n - 1):
            if msg.is_unconcealed(m):
                count_unconcealed += 1
        results.update({candidate: count_unconcealed})
        bar.update(num)
        num += 1

    for key in results.keys():
        print "e = %d; unconcealed = %d" % (key, results.get(key))
    return


def totient_function(n):

    """
    For a given input n, this function returns the value of Euler's Totient function.
    """

    totient_output = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            totient_output += 1
    return totient_output


# solve()


# NOTES:

# View c as a number of the form a**b mod x, and not a variable

# For given p, q, and n, which values of e have the longest period between
# unconcealed messages (for arbitrary messages m)?

# Is 181 special, or will many primes serve as "bad" e candidates?

# Explore totient more.  Which totient values seem to imply "bad" e candidates?
