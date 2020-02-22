function Tree(){
    this.root = null;

    this.addValue = function(val){
        var n = new Node(val);            
        if(this.root == null){
            this.root = n
        }
        else{
            this.root.addNode(n);
        }
    }

    this.traverse = function(){
        return this.root.visit()
    }

    this.inorder = function(){
        return this.root.inorder()
    }

    this.pathToLeaves = function(){
        // console.log('here')
        visitedPath = []
        length = 0
        return this.root.path(visitedPath, length)
        // console.log(this.root)
    }

    this.search = function(val){
        if(this.root == val){
            console.log("found")
        }
        else
            return this.root.search(val, 0)
    }

    this.bfs = function () {
        queue = new Queue()
        info = {}    
        level = 0          
        queue.enqueue(this.root)
        info[queue.getFront().value] = level        

        // console.log(info)
        // breadthResult.push({'data': queue.getFront().value, 'level': level})

        while(!queue.isEmpty()){
            current = queue.getFront()
            toPrint = ''
            // console.log(queue.queue.length)
            console.log(current.value)                        
            if(current.left){
                info[current.left.value] = info[current.value]+1
                queue.enqueue(current.left)
                // console.log(info)
                // breadthResult.push({'data': current.left.value, 'level': level})
            }            
            if(current.right){
                info[current.right.value] = info[current.value]+1
                queue.enqueue(current.right)
                // console.log(info)
                // breadthResult.push({'data': current.right.value, 'level': level})
            }            
            queue.dequeue()                                     
        }     
        console.log(info)
        return info
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

    this.search =function(val, level) {

        if(val==this.value)
            return console.log("found at level: ", level)
        else if(val>this.value){
            if(this.right)
                this.right.search(val, level+1)
            else
                return console.log("not found in right")
        }
        else if(val<this.value){
            if(this.left)
                this.left.search(val, level+1)
            else 
                return console.log("not found in left ")
        }
        else
            return console.log(this.value, val)
    }

}



function Queue(){
    this.queue = []

    this.enqueue = function(val) {
        this.queue.push(val)
    }

    this.dequeue = function() {
        this.queue = this.queue.slice(1,)
    }

    this.getFront = function () {
        return this.queue[0]
    }

    this.isEmpty = function () {
        if(this.queue.length == 0)
            return true
        else  
            return false
    }

}

function setup(){
    // noCanvas();
    tree = new Tree();
    tree.addValue(10);
    tree.addValue(15);
    tree.addValue(5);    
    tree.addValue(3);
    tree.addValue(2);
    tree.addValue(17);
    tree.addValue(16);
    // tree.addValue(0);
    console.log(tree);
    // tree.pathToLeaves();
    tree.search(4);
    tree.bfs();
}

var tree;
setup();