import java.util.PriorityQueue;
import java.util.HashMap;
import java.util.Map;

class Node {
    char ch;
    int frequency;
    Node left, right;

    Node(char ch, int frequency) {
        this.ch = ch;
        this.frequency = frequency;
        left = null;
        right = null;
    }

    Node(int frequency, Node left, Node right) {
        this.ch = '-';
        this.frequency = frequency;
        this.left = left;
        this.right = right;
    }
}

public class HuffmanCoding {

    public static Node buildHuffmanTree(Map<Character, Integer> freqMap) {
        PriorityQueue<Node> pq = new PriorityQueue<>((a, b) -> a.frequency - b.frequency);
        for (Map.Entry<Character, Integer> entry : freqMap.entrySet()) {
            pq.add(new Node(entry.getKey(), entry.getValue()));
        }
        while (pq.size() > 1) {
            Node left = pq.poll();
            Node right = pq.poll();
            int sum = left.frequency + right.frequency;
            pq.add(new Node(sum, left, right));
        }
        return pq.poll();
    }

    public static void generateCodes(Node root, String code, Map<Character, String> huffmanCode) {
        if (root == null) {
            return;
        }
        if (root.left == null && root.right == null) {
            huffmanCode.put(root.ch, code);
        }
        generateCodes(root.left, code + '0', huffmanCode);
        generateCodes(root.right, code + '1', huffmanCode);
    }

    public static String encode(String text, Map<Character, String> huffmanCode) {
        StringBuilder encoded = new StringBuilder();
        for (char ch : text.toCharArray()) {
            encoded.append(huffmanCode.get(ch));
        }
        return encoded.toString();
    }

    public static String decode(String encodedText, Node root) {
        StringBuilder decoded = new StringBuilder();
        Node currentNode = root;
        for (int i = 0; i < encodedText.length(); i++) {
            currentNode = (encodedText.charAt(i) == '0') ? currentNode.left : currentNode.right;
            if (currentNode.left == null && currentNode.right == null) {
                decoded.append(currentNode.ch);
                currentNode = root;
            }
        }
        return decoded.toString();
    }

    public static void main(String[] args) {
        String text = "huffman coding example";
        Map<Character, Integer> freqMap = new HashMap<>();
        for (char ch : text.toCharArray()) {
            freqMap.put(ch, freqMap.getOrDefault(ch, 0) + 1);
        }
        Node root = buildHuffmanTree(freqMap);
        Map<Character, String> huffmanCode = new HashMap<>();
        generateCodes(root, "", huffmanCode);
        System.out.println("Huffman Codes: " + huffmanCode);
        String encodedText = encode(text, huffmanCode);
        System.out.println("Encoded Text: " + encodedText);
        String decodedText = decode(encodedText, root);
        System.out.println("Decoded Text: " + decodedText);
    }
}
