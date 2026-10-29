class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word)) + ","
        encoded_string += "#" + "".join(strs)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        # If 5,5,#HelloWorld -> [5, 5, HelloWorld]
        # decode_string = s.split('#') #5,5 , HelloWorld
        split_index = 0
        while s[split_index] != '#':
            split_index += 1
        raw_string = s[split_index + 1:]
        result_string = []
        start_ind = 0
        words_length = s[0:split_index].split(',')[0:-1]#5, 5
        for i in words_length:
            length = int(i)
            result_string.append(raw_string[start_ind:(start_ind + length)])
            start_ind += length #updated starting index
        return result_string