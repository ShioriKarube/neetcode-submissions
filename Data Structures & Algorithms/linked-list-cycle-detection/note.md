# 解法: フロイド法
フロイド法とはslowとfastの2つのポインタを異なる速さで動かす手法。「一方向に辿れる構造」と「速さの違いから位置関係がわかる」という性質を支える時に応用できる。
例）循環の開始位置を求める、連結リストの真ん中のノードを求める、など

while fast and fast.nextという条件によって空のリストのガードの役目を果たしている。

***
+α 連結リストが回文かどうかを判定するコード
```python
        fast, slow = head, head

        if not head:
            return False
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        cur = slow.next
        slow.next = None
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        while prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next
            
        return True
```
