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

class UnitTesting(MoveSceneCollectionTesting):
    def get_reference_scene_tree_map(self):
        # original tree, no changes
        return self.get_initial_scene_tree_map()

    def test_scene_collection_move_a(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        for collection in tree.values():
            # can't move into master_collection anywhere
            self.assertFalse(master_collection.move_above(collection))

        self.compare_tree_maps()

    def test_scene_collection_move_b(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        for collection in tree.values():
            # can't move into master_collection anywhere
            self.assertFalse(master_collection.move_below(collection))

        self.compare_tree_maps()

    def test_scene_collection_move_c(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        for collection in tree.values():
            # can't move into master_collection anywhere
            self.assertFalse(collection.move_above(master_collection))

        self.compare_tree_maps()

    def test_scene_collection_move_d(self):
        """
        Test outliner operations
        """
        import bpy
        master_collection = bpy.context.scene.master_collection

        tree = self.setup_tree()
        for collection in tree.values():
            # can't move into master_collection anywhere
            self.assertFalse(collection.move_below(master_collection))

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
