class Solution:

    def encode(self, strs: List[str]) -> str:
        new = ''
        if not strs:
            return '_'
        for i,elt in enumerate(strs):
            if i!= len(strs)-1:
                new += f'{elt}_#'
            else:
                new += f'{elt}'
        return new
    def decode(self, s: str) -> List[str]:
        if s == '_':
            return []
        l = s.split('_#')
        return l