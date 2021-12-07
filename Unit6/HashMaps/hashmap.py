"""
hashmap.py
Contains the HashMap ADT
"""
import math
from linkedlist import LinkedList


class HashMap:
    """
    A HashMap used for quickly storing and accessing data

    Atributes:
    ----------
    self.bucket_num : Int
        The number of buckets or
    self._keys : List
        The list of keys not hashed
    self.hash_keys : List<LinkedList>
        The keys for each bucket. List[0] is the keys for the first bucket a
        and so on
    self.values : List<LinkedList>
        The values for each bucket. List[0] is the list of the values
        for the first bucket and so on

    Methods:
    --------
    get(key): Get the value that corresponds with the key
    set(key, value): Create a new pair
    remove(key): Remove the key and its corresponding value
    capacity(): The number of buckets in the Map
    size(): The number of key-value pairs in the Map
    keys(): Return the keys
    clear(): Clears the hashmap and resets the number of buckets
    """

    def __init__(self, bucket_num=7):
        """
        Constructor function

        Paramaters:
        -----------
        bucket_num : Int
            The initial number of buckets. Works best as a prime or odd number
        """
        self.bucket_num = bucket_num

        self._keys = []
        self.hash_keys = [LinkedList() for _ in range(self.bucket_num)]
        self.values = [LinkedList() for _ in range(self.bucket_num)]

        self._size = 0

    def get(self, key):
        """
        Get the value corresponding to the key

        Paramaters:
        -----------
        key : tuple
            The key

        Returns:
        -------
            The value that cooresponds with the key
        """
        hash_key = HashMap.hash(key)
        key_index = hash_key % self.bucket_num

        # If there is a LinkedList at the index
        if not self.hash_keys[key_index].is_empty():
            # If the key is in the LinkedList, return the cooresponding value
            index = self.hash_keys[key_index].find(hash_key)
            return self.values[key_index].get(index)
        raise KeyError("The key is not in the HashMap")

    def set(self, key, value):
        """
        Create a new key-value pair

        Paramaters:
        -----------
        key : tuple
            The key
        value : int
            The value cooresponding with the key
        """
        hash_key = HashMap.hash(key)
        key_index = hash_key % self.bucket_num

        # Add the key to the linked list at the index
        self.hash_keys[key_index].add(hash_key)
        # Add the value to the linked list at the correct index
        self.values[key_index].add(value)

        # Add the key and values to the keys and values list
        self._keys.append(key)

        self._size += 1

        # If 80% of the buckets are full rehash
        if self._load_factor() >= 0.80:
            new_hash = HashMap.rehash(self)
            # Set self to the new hashmap
            self._set_self(new_hash)

    def remove(self, key):
        """
        Remvoves the key and cooresponding value from the HashMap

        Paramaters:
        -----------
        key : tuple
            The key to be removed
        """
        hash_key = HashMap.hash(key)
        key_index = hash_key % self.bucket_num

        # If the linked list is not empty
        if not self.hash_keys[key_index].is_empty():
            # Verify that the key value is in linked list
            try:
                self.hash_keys[key_index].find(hash_key)
            except ValueError:
                return
            # Remove the cooresponding value from values cataloug
            # Remove the key from the linked list
            self.hash_keys[key_index].remove(hash_key)
            # Remove the key from the keys cataloug
            self._keys.remove(key)

        self._size += 1

    def capacity(self):
        """
        Return the total number of buckets in the HashMap

        Returns:
        --------
        int
            The number of buckets in the HashMap
        """
        return self.bucket_num

    def size(self):
        """
        Return the number of key-value pairs in the HashMap

        Returns:
        --------
        int
            The number of pairs in the HashMap
        """
        return self._size

    def keys(self):
        """
        Return a list of all keys

        Returns:
        --------
        List<tuple>
            The list of keys
        """
        return self._keys

    def clear(self, bucket_num=7):
        """
        Clears the HashMap and resets the number of buckets

        Paramaters:
        -----------
        bucket_num : int
            The number of buckets. Defaults to 7 (A prime number)
        """
        self.bucket_num = bucket_num

        self.hash_keys = [LinkedList() for _ in range(self.bucket_num)]
        self.values = [LinkedList() for _ in range(self.bucket_num)]
        self._keys = []

        self._size = 0

    def _load_factor(self):
        """
        Calculates the load factor of the HashMap,
        namely (The number of used buckets) / (total number of buckets)

        Returns:
        --------
        the load factor : Float
        """
        # The number of LinkedLists that contain data
        num_full = sum([1 * (0 if x.is_empty() else 1)
                       for x in self.hash_keys])

        return num_full / self.bucket_num

    def _set_self(self, hashmap):
        """
        Sets self into the given hashmap

        Paramaters:
        -----------
        hashmap : HashMap
            The new hashmap
        """
        self.bucket_num = hashmap.capacity()

        self.hash_keys = hashmap.hash_keys
        self.values = hashmap.values
        self._keys = hashmap.keys()

        self._size = hashmap.size()

    @staticmethod
    def rehash(hashmap):
        """
        Creates a new hash with more buckets

        Paramaters:
        -----------
        hashmap : HashMap
            The hashmap being make larger

        Returns:
        --------
        Hashmap
            Same hashmap, but more buckets
        """
        current_capacity = hashmap.capacity()
        new_capacity = HashMap.next_prime(current_capacity)

        new_hashmap = HashMap(new_capacity)

        keys = hashmap.keys()

        # Add the old key-value pairs into the new hashmap
        for key in keys:
            new_hashmap.set(key, hashmap.get(key))

        return new_hashmap

    @staticmethod
    def next_prime(last_prime):
        """
        Finds the next prime number after a given input

        Paramaters:
        -----------
        last_prime : int
            The lower bound for prime number search
        """
        def is_prime(number):
            """
            Returns True if number is prime
            """
            if number <= 1:
                return False

            for x in range(2, math.ceil(math.sqrt(number) + 1)):
                # If number is divisable by anything, return false
                if number % x == 0:
                    return False
            return True

        prime_found = False
        while not prime_found:
            last_prime += 1
            prime_found = is_prime(last_prime)

        return last_prime

    @staticmethod
    def hash(object):
        """
        A method used for generating a hash of a non-mutable iterable object

        Paramaters:
        -----------
        object : Object (must be non-mutable and iterative)
            The object we are generating a hash for

        Return:
        -------
        Int:
            The hash value of x
        """
        hash_value = 0
        for i, x in enumerate(object):
            # If the object is a string, add the ordinal value to the hash
            if isinstance(x, str):
                hash_value += ord(x) * (i + 1)
            # If the object is an integer, add it to the hash value
            elif isinstance(x, int):
                hash_value += x * (i + 1)
            # If the object is a float, treat it as a tuple: 65.43 => (65, 43)
            elif isinstance(x, float):
                x = str(x).split('.')
                hash_value += HashMap.hash((x[0], x[1])) * (i + 1)
            # If the object is iterative, run the hash on it
            elif type(x) in [tuple, set, list]:
                hash_value += HashMap.hash(x) * (i + 1)
            # If the object is a custom object
            else:
                hash_value += x.__hash__() * (i + 1)

        return hash_value
