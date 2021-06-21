from ll_zip import __version__


def test_version():
    assert __version__ == '0.1.0'

# from ll_zip.ll_zip import  zipLists
# from ll_zip.ll_zip import Node,LinkedList


# def test_one():
#     ll1 = LinkedList()
#     ll1.append(7)
#     ll1.append(9)
#     ll2 = LinkedList()
#     ll2.append(1)

#     actual = str(zipLists(ll1,ll2))
#     expected = f'{{7}}->{{1}}->{{9}}->None'
#     assert actual==expected



# def test_tow():
#     ll1 = LinkedList()
#     ll2 = LinkedList()
#     ll2.append(9)
#     ll2.append(7)

#     actual = str(zipLists(ll1,ll2))
#     expected =f'{{9}}->{{7}}->None'
#     assert actual==expected



# def test_three():
#     ll1 = LinkedList()
#     ll1.append(7)
#     ll2 = LinkedList()
#     ll2.append(9)
#     ll2.append(1)

#     actual = str(zipLists(ll1,ll2))
#     expected = f'{{7}}->{{9}}->{{1}}->None'
#     assert actual==expected


# def test_four():
#     ll1 = LinkedList()
#     ll1.append(9)
#     ll1.append(7)
#     ll2 = LinkedList()
    

#     actual = str(zipLists(ll1,ll2))
#     expected =f'{{9}}->{{7}}->None'
#     assert actual==expected


# def test_five():
#     ll1 = LinkedList()


#     ll2 = LinkedList()
#     ll2.append(9)

#     actual = str(zipLists(ll1,ll2))
#     expected =f'{{9}}->None'
#     assert actual==expected
