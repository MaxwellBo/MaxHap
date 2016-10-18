import itertools

def main():

    # These should be modified by you
    parps = ["1", "2", "3"] # PARticiPantS

    countries = set(["a", "b", "c"])

    prefs_list = [ ["a", "b", "c"]
                 , ["c", "b", "a"] 
                 , ["b", "a", "c"]
                 ]


    # Sanity Checks
    for prefs in prefs_list:
        for pref in prefs:
            assert(pref in countries)

    assert(len(prefs) == len(parps))

    # The actual algorithm

    def hapiness(perm):
        total = 0

        for i, perm_pref in enumerate(perm):
            try:
                # Need to reverse this so that the most valuable preferences
                # give the highest index
                total += prefs_list[i][::-1].index(perm_pref)
            except:
                pass

        return total


    perms = itertools.permutations(countries)

    # Low hapiness comes first
    sorted_perms = sorted(perms, key=hapiness)

    for i, _ in enumerate(parps):
        # Taking the last element --> highest hapiness
        print(parps[i], sorted_perms[-1][i])

if __name__ == '__main__':
    main()