class Solution(object):
    def buildTree(self, preorder, inorder):
        def buildTreeHelper(preorder,pstart,pend,inorder,istart,iend,indexDict):
            if pstart>pend or istart>iend:
                return None
            root=TreeNode(preorder[pstart])
            rindex=indexDict.get(preorder[pstart])
            # prestart+length of part sub tree (rindex-istart)
            left=buildTreeHelper(preorder,pstart+1,pstart+rindex-istart,inorder,istart,rindex-1,indexDict)
            right=buildTreeHelper(preorder,pstart+rindex-istart+1,pend,inorder,rindex+1,iend,indexDict)
            root.left=left
            root.right=right
            return root
        
        if not inorder or not preorder:
            return None
        if len(inorder)!=len(preorder):
            return None
        # index map
        indexDict={}
        for i in xrange(len(inorder)):
            indexDict[inorder[i]]=i
        
        return buildTreeHelper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,indexDict)
