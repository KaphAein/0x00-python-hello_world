#!/usr/bin/python3
"""Define a class Node"""


class Node:
    """Represents a Node in a list"""
    def __init__(self, data, next_node=None):
        """Represents private attributes

        Args:
        data (int): The data of the new Node.
        next_node (Node): The next node of the new Node.
        """
        Node.data = data
        Node.next_node = next_node

    @property
    def data(self):
        """Represents data attribute getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Represents data attribute setter"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Represents next_node attribute getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Represents next_node attribute setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a LinkedList class"""


class SinglyLinkedList:
    """Represents a Linked List"""
    def __init__(self):
        """Represents private attributes"""
        self.__head = None

    def sorted_insert(self, value):
        """Method to add nodes in a sorted list
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)

        if self.__head is None or self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
            return
        else:
            current = self.__head
            while (current.next_node and current.next_node.data < new.data):
                current = current.next_node

            new.next_node = current.next_node
            current.next_node = new


    def __str__(self):
        """Method to print nodes in a sorted list"""
        current = self.__head
        new_list = []
        while current:
            new_list.append(str(current.data))
            current = current.next_node
        return '\n'.join(new_list)
