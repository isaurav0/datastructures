var tree;

function setup(){
    // noCanvas();
    tree = new Tree();
    // for(i=1;i<=5;i++){
    //     tree.addValue(Math.floor(Math.random()*10))
    //     // tree.addValue(i)
    // }
    // tree.inorder();
    tree.addValue(5);
    tree.addValue(3);
    tree.addValue(6);
    tree.addValue(2);
    tree.addValue(4);
    // tree.addValue(8)
    // tree.addValue(9)
    console.log(tree);
    tree.path();
}

function Tree(){
    this.root = null;
}

Tree.prototype.addValue = function(val){
    var n = new Node(val);            
    if(this.root == null){
        this.root = n
    }
    else{
        this.root.addNode(n);
    }
}

Tree.prototype.traverse = function(){
    return this.root.visit()
}

Tree.prototype.inorder = function(){
    return this.root.inorder()
}

Tree.prototype.path = function(){
    // console.log('here')
    visitedPath = []
    length = 0
    return this.root.path(visitedPath, length)
    // console.log(this.root)
}



function Node(val){
    this.value = val
    this.left = null
    this.right = null

    this.addNode = function(node){
        if(this.value == node.value){
            return false
        }
        else if(node.value > this.value){
            if(this.right){
                return this.right.addNode(node)
            }
            else{
                this.right = node
                return true
            }            
        }
        else{
            if(this.left){
                return this.left.addNode(node)
            }
            else{
                this.left = node
                return true
            }
            
        }
    }

    this.visit = function(){
        if(this.left)
            this.left.visit();
        console.log(this.value)
        if(this.right)
            this.right.visit();
    }

    this.inorder = function(){
            if(this.left)
                this.left.inorder()
            console.log(this.value)
            if(this.right)
                this.right.inorder()
    }

    this.path = function(visitedPath, length){
        if(this == null)
            return console.log("nothing here ")

        visitedPath[length] = this.value
        length++;

        
        if(this.left == null && this.right == null)
            console.log(visitedPath.slice(0,length))
        if(this.left) 
            this.left.path(visitedPath, length)
        if(this.right){            
            this.right.path(visitedPath, length)
        }
    }
}


setup();