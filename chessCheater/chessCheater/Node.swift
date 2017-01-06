//
//  Node.swift
//  chessCheater
//
//  Created by Will Rollins on 1/6/17.
//  Copyright © 2017 Will Rollins. All rights reserved.
//

import Foundation

// we used class in swift so that we could pass by reference


//ToDo: do we need move to be within the node?
public class Node {
    //total bytes of node = 8 * # of variables = 72 bytes
    
    var bBoard: Int
    var wBoard: Int
    var pawns: Int
    var rooks: Int
    var bishops: Int
    var knights: Int
    var king: Int
    var queen: Int
    var move: Int
    var left: Node?
    var right: Node?
    
    //initializer
    init(bBoard: Int, wBoard: Int, pawns: Int, rooks: Int, bishops: Int, knights: Int, king: Int, queen: Int, move: Int) {
        self.bBoard = bBoard
        self.wBoard = wBoard
        self.pawns = pawns
        self.rooks = rooks
        self.bishops = bishops
        self.knights = knights
        self.king = king
        self.queen = queen
        self.move = move
        self.left = nil
        self.right = nil
        
    }
    
    //ToDo: write search methods
    //would this be faster in another class as we would not have to store it within the lines of the cache
    
    
    
}
