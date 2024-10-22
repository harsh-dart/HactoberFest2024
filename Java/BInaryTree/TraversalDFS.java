class TreeNode {
    int val;
    TreeNode left, right;

    TreeNode(int item) {
        val = item;
        left = right = null;
    }
}

public class TraversalDFS {
    TreeNode root;

    void dfsTraversal(TreeNode node) {
        if (node == null) return;

        System.out.print(node.val + " ");
        dfsTraversal(node.left);
        dfsTraversal(node.right);
    }

    public static void main(String[] args) {
        TraversalDFS tree = new TraversalDFS();
        tree.root = new TreeNode(1);
        tree.root.left = new TreeNode(2);
        tree.root.right = new TreeNode(3);
        tree.root.left.left = new TreeNode(4);
        tree.root.left.right = new TreeNode(5);

        tree.dfsTraversal(tree.root);
    }
}
