class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_live = timeToLive
        self.hsh = dict()


    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.hsh:
            self.hsh[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.hsh:
            if self.hsh[tokenId] + self.time_live > currentTime:
                self.hsh[tokenId] = currentTime
            else:
                del self.hsh[tokenId]

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for token in self.hsh:
            if self.hsh[token] + self.time_live > currentTime:
                cnt += 1

        return cnt

