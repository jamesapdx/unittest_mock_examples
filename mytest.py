#!/usr/bin/bash

import unittest
import mock
import mymoc
from mock import patch

class Mytest(unittest.TestCase):

    def test_func_main(self):
        obj_mocked = mock.Mock()
        # obj_mocked.__repr__ = mock.Mock(return_value="55")
        print(type(obj_mocked))
        # obj_mocked.__repr__ = "asd"
        mymoc.fun_called = mock.Mock()
        mymoc.fun_main(obj_mocked)
        mymoc.fun_called.assert_called_with(obj_mocked, "bb")

# 1> basic unit test
    def test_basic_return_pass(self):
        x = mymoc.basic_return(2)
        self.assertEqual(x, 5)

### Standard import and call
# 2. import method
    def test_string_function_import_pass(self):
        import string
        string.lower = mock.Mock(return_value="i am lower")
        string.replace =  mock.Mock(return_value="i am lower")
        x = mymoc.string_function("I AM UPPER")
        # string.lower.assert_called_with(["I AM UPPER"])
        self.assertEqual(x, "i am lower")

# 3) as a patch
    @patch('mymoc.string.lower')
    def test_string_function_patch_pass(self, str_p):
        # string.lower = mock.Mock(return_value="eee")
        str_p.return_value = "i am lower"
        x = mymoc.string_function("I AM UPPER")
        self.assertEqual(x, "i am lower")

### From x import y
# 4] import method, FAILS!
    def test_random_function_import_pass(self):
        return
        from random import random
        random = mock.Mock(return_value=2000)
        x = mymoc.random_function()
        self.assertEqual(x, 2000)

# 5- patch method, MUST USE
    @patch('mymoc.random')
    def test_random_function_patch_pass(self, rand_p):
        rand_p.return_value = 2000
        x = mymoc.random_function()
        self.assertEqual(x, 2000)

    def test_host_is_adapter_up(self):
        self.host = mymoc.Host()
        self.host.adapter.is_up = mock.Mock(return_value="upup")
        x = self.host.is_adapter_up1()
        self.assertEqual(x, "upup")

    def test_host_is_adapter2_up(self):
        self.host = mymoc.Host()
        # mymoc.Adapter = mock.Mock()
        mymoc.Adapter.is_up = mock.Mock(return_value="upup")
        self.assertEqual(self.host.is_adapter_up2(), "upup")

if __name__ == "__main__":

    unittest.main()

