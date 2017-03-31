# ############################################################
# Importing - Same For All Render Layer Tests
# ############################################################

from render_layer_common import *
import unittest
import os
import sys

sys.path.append(os.path.dirname(__file__))


# ############################################################
# Testing
# ############################################################

class UnitTesting(MoveLayerCollectionTesting):
    def get_reference_scene_tree_map(self):
        # original tree, no changes
        return self.get_initial_scene_tree_map()

    def get_reference_layers_tree_map(self):
        # original tree, no changes
        return self.get_initial_layers_tree_map()

    def test_layer_collection_into(self):
        """
        Test outliner operations
        Prevent collection from being dragged into itself
        """
        self.setup_tree()
        self.assertFalse(self.move_into("Layer 2.dog", "Layer 2.3.dog"))
        self.compare_tree_maps()


# ############################################################
# Main - Same For All Render Layer Tests
# ############################################################

if __name__ == '__main__':
    import sys

    extra_arguments = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    sys.argv = [__file__] + (sys.argv[sys.argv.index("--") + 2:] if "--" in sys.argv else [])

    UnitTesting._extra_arguments = extra_arguments
    unittest.main()
