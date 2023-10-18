our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)
our_dict["d"] = our_list[4]
our_list.pop(4)
my_tuple = ()
for i in our_dict:
    m_tuple = (our_dict[i],)
    my_tuple += m_tuple
print(our_list)
print(our_dict)
print(my_tuple)
print(our_tuple)
if(my_tuple==our_tuple):
    print("tuples are the same.")