#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 16:09:29 2019

@author: Gayatri
"""

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class Linklist:
    def __init__(self, data):
        node = Node(data)
        self.head = node
        

def insert_node_begininnig(ll, node):
    node.next = ll.head
    ll.head = node


def insert_node_end(ll, node):
    temp = ll.head
    while temp.next != None:
        temp = temp.next
    temp.next = node


def insert_node_after(node_new, node_after):
    node_new.next = node_after.next
    node_after.next = node_new


def delete_node(ll, node):
    tmp = ll.head
    if tmp == node:
        ll.head = ll.head.next
        del node
    else:
        while tmp.next != None:
            if tmp.next == node:
                tmp.next = node.next
                del node
                break
            tmp = tmp.next


def traverse(ll):
    tmp = ll.head
    while tmp.next != None:
        print(tmp.data)
        tmp=tmp.next
    print(tmp.data)


if __name__ == "__main__":
    ll = Linklist(10)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    
    traverse(ll)
    
    insert_node_begininnig(ll, node1)
    traverse(ll)
    
    insert_node_end(ll, node2)
    traverse(ll)
    
    delete_node(ll, ll.head.next)
    traverse(ll)
