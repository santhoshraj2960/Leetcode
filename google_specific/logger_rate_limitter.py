# https://leetcode.com/problems/logger-rate-limiter/

class Logger:

    def __init__(self):
        self.message_timestamp_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.message_timestamp_map:
            last_print_time = self.message_timestamp_map[message]

            if timestamp >= last_print_time + 10:
                self.message_timestamp_map[message] = timestamp
                return True
            else:
                return False

        else:
            self.message_timestamp_map[message] = timestamp
            return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
