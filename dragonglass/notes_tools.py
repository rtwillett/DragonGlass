class ObsidianNote:
    '''
    Compiles and writes an obsidian notes
    '''
    
    def __init__(self, label, vault_path = '.'): 
        
        self.label = label
        self.vault_path = vault_path
        self.notes = []
        
    def add_header(self, title, level = 2): 

        # Sets min/max values allowable for setting levels
        if level < 1: 
            level = 1
        elif level > 5:
            level = 5

        header = '\n' + '#'*level + f' {title}'
        self.notes.append(header)
    
    def add_text(self, text): 
        self.notes.append(text)
        
    def compile_notes(self):
        self.note_record = '\n'.join(self.notes)
        
    def write_note(self):

        self.compile_notes()
        
        with open(f'{self.vault_path}{self.label}.md', 'w') as f: 
            f.write(self.note_record)
        
        
class DeleteObsidianNote:
    '''
    Removes an obsidian note from a vault
    '''
    
    def __init__(self, label, vault_path = '.'): 
        
        self.label = label
        self.vault_path = vault_path
        
    def delete_note(self): 
        import os
        note_name = f'{self.vault_path}{self.label}.md'
        os.remove(note_name)
        
        
