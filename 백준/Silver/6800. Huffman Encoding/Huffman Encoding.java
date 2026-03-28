import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        Character val;
        Node left, right;
        boolean is_leaf;
        Character c;

        Node(Character val, boolean is_leaf, Character c) {
            this.val = val;
            this.left = null;
            this.right = null;
            this.is_leaf = is_leaf;
            this.c = c;
        }

        void addChild(Node child) {
            if (child.val == '0') this.left = child;
            else this.right = child;
        }
    }

    static class Tree {
        Node root;

        Tree(Node root) {
            this.root = root;
        }

        void insert(char c, String code) {
            Node cur = this.root;
            for (int i = 0; i < code.length(); i++) {
                char ch = code.charAt(i);
                if ((ch == '0' && cur.left == null) || (ch == '1' && cur.right == null)) {
                    cur.addChild(new Node(ch, false, null));
                }
                cur = ch == '0' ? cur.left : cur.right;
            }
            cur.is_leaf = true;
            cur.c = c;
        }

        void search(String code) {
            ArrayList<Character> res = new ArrayList<>();
            int idx = 0;
            Node cur = this.root;
            Node nxt;
            while (idx < code.length()) {
                char ch = code.charAt(idx);
                nxt = ch == '0' ? cur.left : cur.right;
                if (nxt.is_leaf) {
                    res.add(nxt.c);
                    cur = this.root;
                } else {
                    cur = nxt;
                }
                idx++;
            }
            for (char r: res) {
                System.out.print(r);
            }
            System.out.println();
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        Node root = new Node(null, false, null);
        Tree tree = new Tree(root);

        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            String[] inputs = br.readLine().split(" ");
            char c = inputs[0].charAt(0);
            String code = inputs[1];
            tree.insert(c, code);
        }
        String sequence = br.readLine();
        tree.search(sequence);

        // bw.flush();
        // bw.close();
        br.close();
    }
}