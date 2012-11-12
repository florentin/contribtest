import unittest
import os
import generate

class GenerateTestCase(unittest.TestCase):
    def setUp(self):
        self.input_path = "./test/source/"
        self.output_path = "/tmp/contribtext/"
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        self.path_to_test = os.path.abspath(os.path.dirname(__file__))
        
    def tearDown(self):
        for root, dirs, files in os.walk(self.output_path, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.output_path)

    def test_normal(self):
        response = generate.generate_site(self.input_path, self.output_path)
        self.assertIs(response, None)
        
        with open(os.path.join(self.path_to_test, "test/expected_output/contact.html")) as fexpected:
            with open(os.path.join(self.output_path, "contact.html")) as fgenerated:
                expected_html = fexpected.read()
                generated_html = fgenerated.read()
        
        self.assertEqual(generated_html, expected_html)
    
    def test_abnormal(self):
        self.assertRaises(TypeError, generate.generate_site, *("", ))
        failing_args = [
                    ("", ""),
                    ("", self.output_path),
                    (self.input_path, ""),
                    (self.input_path+"/bad", self.output_path),
                    ("/tmp", self.output_path),
                    (self.input_path, self.output_path+"/bad")
        ]
        for args in failing_args:
            self.assertRaises(RuntimeError, generate.generate_site, *args)

    
if __name__ == '__main__':
    unittest.main()
