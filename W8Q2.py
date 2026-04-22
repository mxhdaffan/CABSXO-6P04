from sage.categories.groups import Groups

G = Integers(7)
units = G.unit_group()

print("Set = ", list(G))

print("\nGroup: ", units in Groups())
print("Ring: ", G.is_ring())
print("Field: ", G.is_field())