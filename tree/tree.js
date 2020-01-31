var tree;

function setup(){
    // noCanvas();
    tree = new Tree();
    for(i=0;i<6;i++){
        tree.addValue(Math.floor(Math.random()*10))
    }
    console.log(tree);
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

}


setup();