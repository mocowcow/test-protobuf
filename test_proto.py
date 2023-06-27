import myproto_pb2 as pb

# create a dog
first_dog = pb.Dog()
first_dog.name = "jack"
first_dog.age = 24
first_dog.color = "black"

# serialize the dog
serial = first_dog.SerializeToString()
print(">>serialized dog")
print(serial)

# then deserialize the dog
deserial_dog = pb.Dog()
deserial_dog.ParseFromString(serial)
print(">>deserialized dog")
print(deserial_dog)

# create a dog group
dog_group = pb.DogGroup()
dog_group.name = "crazy doge"

# add first dog into the group
dog_group.dogs.append(first_dog)

# create second dog
# then add into the group
second_dog = dog_group.dogs.add()
second_dog.name = "bob"
second_dog.color = "white"
print(">>dog group")
print(dog_group)
