import unittest
import collections


def sort_prehash(word):
    return ''.join(sorted(word))


def count_letters_prehash(word):
    return tuple(collections.Counter(word).items())


def group_anagrams(words, hash_function):
    result = {}
    for w in words:
        s = hash_function(w.lower())
        if s in result:
            result[s] |= {w}
        else:
            result[s] = {w}
    return result.values()

print group_anagrams(['star','tars','cat','tac','test','stet','cheese','act','coin','icon','arts'], sort_prehash)
print group_anagrams(['star','tars','cat','tac','test','stet','cheese','act','coin','icon','arts'], count_letters_prehash)

exit()


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.tests = [
                        {
                        'input': ['star','tars','cat','tac','test','stet','cheese','act','coin','icon','arts'],
                        'output':[{'star', 'tars', 'arts'}, {'test', 'stet'}, {'cheese'}, {'coin', 'icon'}, {'cat', 'tac', 'act'}]
                        },
                      {
                        'input': ['t','t'],
                        'output':[{'t'}]
                      }
                     ]

    def test_solution_1(self):
        for i in range(1):
            for t in self.tests:
                result = group_anagrams(t['input'], sort_prehash);
                print result;
                self.assert_(sorted(t['output'])==sorted(result), "Test failed!")

    def test_solution_2(self):
        for i in range(1):
            for t in self.tests:
                result = group_anagrams(t['input'], count_letters_prehash);
                print result;
                self.assert_(sorted(t['output'])==sorted(result), "Test failed!")

if __name__ == '__main__':
    unittest.main()
