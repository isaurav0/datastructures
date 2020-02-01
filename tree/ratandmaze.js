function Tree(){
    this.root = null    
    this.makeMaze = function(maze){
        x = 0
        y = 0
        count = 0
        this.root = new Node(maze[0][0], x, y)
        return this.root.makeNode(maze, x, y)              
    }
}

function Node(val){
    this.value = val
    this.x = x
    this.y = y
    this.left = null 
    this.right = null 

    this.makeNode = function(maze, x, y, count){
        if(count == )
    }

}

function main(){
    var maze = [ [1, 1, 1],
                 [1, 0, 1],
                 [1, 0, 1]];

    var tree = new Tree();
    tree.makeMaze(maze);
    console.log(tree)

}

main();