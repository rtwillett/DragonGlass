class CreateVault:
    
    '''Implement this using JSON instead of strings'''
    
    app = '''{}'''
    appearance = '''{"accentColor": ""}'''
    core_plugins = '''[
      "file-explorer",
      "global-search",
      "switcher",
      "graph",
      "backlink",
      "outgoing-link",
      "tag-pane",
      "page-preview",
      "daily-notes",
      "templates",
      "note-composer",
      "command-palette",
      "editor-status",
      "starred",
      "outline",
      "word-count",
      "file-recovery"
    ]'''
    hotkeys = '''{}'''
    workspace = '''{
      "main": {
        "id": "8aed520194abf3eb",
        "type": "split",
        "children": [
          {
            "id": "45bfdcf1e0fa47b6",
            "type": "tabs",
            "children": [
              {
                "id": "e990c028fa712e4f",
                "type": "leaf",
                "state": {
                  "type": "markdown",
                  "state": {
                    "file": "Summarization.md",
                    "mode": "source",
                    "source": false
                  }
                }
              }
            ]
          }
        ],
        "direction": "vertical"
      },
      "left": {
        "id": "c9c64e2ead6eba51",
        "type": "split",
        "children": [
          {
            "id": "e5dfce9788b2fa08",
            "type": "tabs",
            "children": [
              {
                "id": "b30882a23a0433a8",
                "type": "leaf",
                "state": {
                  "type": "file-explorer",
                  "state": {
                    "sortOrder": "alphabetical"
                  }
                }
              },
              {
                "id": "6d32b5ad2626c7da",
                "type": "leaf",
                "state": {
                  "type": "search",
                  "state": {
                    "query": "",
                    "matchingCase": false,
                    "explainSearch": false,
                    "collapseAll": false,
                    "extraContext": false,
                    "sortOrder": "alphabetical"
                  }
                }
              },
              {
                "id": "53d68af5d775370c",
                "type": "leaf",
                "state": {
                  "type": "starred",
                  "state": {}
                }
              }
            ]
          }
        ],
        "direction": "horizontal",
        "width": 300
      },
      "right": {
        "id": "9e4f5725944da2de",
        "type": "split",
        "children": [
          {
            "id": "eb8ed2129fef6656",
            "type": "tabs",
            "children": [
              {
                "id": "c5777f996b2f109f",
                "type": "leaf",
                "state": {
                  "type": "backlink",
                  "state": {
                    "file": "Summarization.md",
                    "collapseAll": false,
                    "extraContext": false,
                    "sortOrder": "alphabetical",
                    "showSearch": false,
                    "searchQuery": "",
                    "backlinkCollapsed": false,
                    "unlinkedCollapsed": frue
                  }
                }
              },
              {
                "id": "560803bf50391c11",
                "type": "leaf",
                "state": {
                  "type": "outgoing-link",
                  "state": {
                    "file": "Summarization.md",
                    "linksCollapsed": false,
                    "unlinkedCollapsed": true
                  }
                }
              },
              {
                "id": "8514c368c3868c61",
                "type": "leaf",
                "state": {
                  "type": "tag",
                  "state": {
                    "sortOrder": "frequency",
                    "useHierarchy": true
                  }
                }
              },
              {
                "id": "50d41e589670e7b3",
                "type": "leaf",
                "state": {
                  "type": "outline",
                  "state": {
                    "file": "Summarization.md"
                  }
                }
              }
            ]
          }
        ],
        "direction": "horizontal",
        "width": 300,
        "collapsed": true
      },
      "active": "e990c028fa712e4f",
      "lastOpenFiles": [
        "Gryphon Strategies.md",
        "OSINT.md",
        "Summarization.md"
      ]
    }'''

    def __init__(self, vault_dir = None): 
        
        import os

        if vault_dir is None:
          self.vault_dir = os.getcwd()
        else: 
          self.vault_dir = vault_dir
        
        
    def create_vault(self, vault_name): 
        from os import mkdir
        from os.path import exists
        
        vault_fp = f'{self.vault_dir}/{vault_name}'
        config_fp = f'{vault_fp}/.obsidian'
        
        if not exists(f'{self.vault_dir}/{vault_name}'):
            mkdir(vault_fp)
            mkdir(config_fp)
            
        # Creates the configuration files in the .obsidian folder to define the settings of the Obsidian Vault

        with open(f'{config_fp}/app.json', mode='w') as f:
            f.write(self.app)
            
        with open(f'{config_fp}/appearance.json', mode='w') as f:
            f.write(self.appearance)
            
        with open(f'{config_fp}/core-plugins.json', mode='w') as f:
            f.write(self.core_plugins)
            
        with open(f'{config_fp}/hotkeys.json', mode='w') as f:
            f.write(self.hotkeys)
            
        with open(f'{config_fp}/workspace.json', mode='w') as f:
            f.write(self.workspace)



class MountVault:
    
    def __init__(self, vault, vault_path = '.'):
        self.vault = vault
        self.vault_path = f'{vault_path}/{vault}/'
        
        self.get_notes()
        
    # def make_note(self, note_name, note_text): 
        
    #     with open(f'{self.vault_path}/{note_name}.md', mode='w') as f:
    #         f.write(note_text)
    
    def get_notes(self): 
        '''
        Reads the markdown files in a vault and provides those in a list as an attribute
        '''
        
        from glob import glob
        import re
        
        self.notes = [f.split('/')[-1].split('.')[0] for f in glob(f'{self.vault_path}*.md') if re.search('\.md$', f)]