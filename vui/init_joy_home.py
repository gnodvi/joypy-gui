'''
Utility module to help with setting up the initial contents of the
JOY_HOME directory.

These contents are kept in this Python module as a base64-encoded zip
file, so you can just do, e.g.:

    import init_joy_home
    init_joy_home.initialize(JOY_HOME)

'''
import base64
import StringIO
import zipfile


def initialize(joy_home):
    Z.extractall(joy_home)


def create_data(from_dir='./default_joy_home'):
    f = StringIO.StringIO()
    z = zipfile.ZipFile(f, mode='w')
    for fn in os.listdir(from_dir):
        from_fn = os.path.join(from_dir, fn)
        z.write(from_fn, fn)
    z.close()
    return base64.encodestring(f.getvalue())


Z = zipfile.ZipFile(StringIO.StringIO(base64.decodestring('''\
UEsDBBQAAAAAACdbd0wAAAAAAAAAAAAAAAAHAAAAbG9nLnR4dFBLAwQUAAAAAAAnW3dMd3+aXgMA
AAADAAAADAAAAHN0YWNrLnBpY2tsZSh0LlBLAwQUAAAAAAAqYHdMmVSdh2QGAABkBgAACgAAAGxp
YnJhcnkucHknJycKVGhpcyBmaWxlIGlzIGV4ZWNmaWxlKCknZCB3aXRoIGEgbmFtZXNwYWNlIGNv
bnRhaW5pbmc6CgogIEQgLSB0aGUgSm95IGRpY3Rpb25hcnkKICBkIC0gdGhlIERpc3BsYXkgb2Jq
ZWN0CiAgcHQgLSB0aGUgUGVyc2lzdFRhc2sgb2JqZWN0CiAgbG9nIC0gdGhlIGxvZy50eHQgdmll
d2VyCiAgbG9vcCAtIHRoZSBUaGVMb29wIG1haW4gbG9vcCBvYmplY3QKICBzdGFja19ob2xkZXIg
LSB0aGUgUHl0aG9uIGxpc3Qgb2JqZWN0IHRoYXQgaG9sZHMgdGhlIEpveSBzdGFjayB0dXBsZQog
IHdvcmxkIC0gdGhlIEpveSBlbnZpcm9ubWVudAoKJycnCmZyb20gam95LmxpYnJhcnkgaW1wb3J0
IEZ1bmN0aW9uV3JhcHBlciwgU2ltcGxlRnVuY3Rpb25XcmFwcGVyCmZyb20gam95LnV0aWxzLnN0
YWNrIGltcG9ydCBsaXN0X3RvX3N0YWNrLCBwdXNoYmFjawoKCmRlZiBpbnN0YWxsKGNvbW1hbmQp
OiBEW2NvbW1hbmQubmFtZV0gPSBjb21tYW5kCgoKQGluc3RhbGwKQFNpbXBsZUZ1bmN0aW9uV3Jh
cHBlcgpkZWYgZ29vZF92aWV3ZXJfbG9jYXRpb24oc3RhY2spOgogICAgdmlld2VycyA9IGxpc3Qo
ZC5pdGVyX3ZpZXdlcnMoKSkKICAgIGlmIHZpZXdlcnM6CiAgICAgICAgdmlld2Vycy5zb3J0KGtl
eT1sYW1iZGEgKFYsIHgsIHkpOiBWLncgKiBWLmgpCiAgICAgICAgViwgeCwgeSA9IHZpZXdlcnNb
LTFdCiAgICAgICAgY29vcmRzID0gKHggKyAxLCAoeSArIFYuaCAvIDIsICgpKSkKICAgIGVsc2U6
CiAgICAgICAgY29vcmRzID0gKDAsICgwLCAoKSkpCiAgICByZXR1cm4gY29vcmRzLCBzdGFjawoK
CkBpbnN0YWxsCkBGdW5jdGlvbldyYXBwZXIKZGVmIGNtcF8oc3RhY2ssIGV4cHJlc3Npb24sIGRp
Y3Rpb25hcnkpOgogICAgTCwgKEUsIChHLCAoYiwgKGEsIHN0YWNrKSkpKSA9IHN0YWNrCiAgICBl
eHByZXNzaW9uID0gcHVzaGJhY2soRyBpZiBhID4gYiBlbHNlIEwgaWYgYSA8IGIgZWxzZSBFLCBl
eHByZXNzaW9uKQogICAgcmV0dXJuIHN0YWNrLCBleHByZXNzaW9uLCBkaWN0aW9uYXJ5CgoKQGlu
c3RhbGwKQFNpbXBsZUZ1bmN0aW9uV3JhcHBlcgpkZWYgbGlzdF92aWV3ZXJzKHN0YWNrKToKICAg
IGxpbmVzID0gW10KICAgIGZvciB4LCBUIGluIGQudHJhY2tzOgogICAgICAgIGxpbmVzLmFwcGVu
ZCgneDogJWksIHc6ICVpLCAlcicgJSAoeCwgVC53LCBUKSkKICAgICAgICBmb3IgeSwgViBpbiBU
LnZpZXdlcnM6CiAgICAgICAgICAgIGxpbmVzLmFwcGVuZCgnICAgIHk6ICVpLCBoOiAlaSwgbmFt
ZTogJXMsICVyJyAlICh5LCBWLmgsIFYuY29udGVudF9pZCwgVikpCiAgICByZXR1cm4gJ1xuJy5q
b2luKGxpbmVzKSwgc3RhY2sKCgpAaW5zdGFsbApAU2ltcGxlRnVuY3Rpb25XcmFwcGVyCmRlZiBz
cGxpdGxpbmVzKHN0YWNrKToKICAgIHRleHQsIHN0YWNrID0gc3RhY2sKICAgIGFzc2VydCBpc2lu
c3RhbmNlKHRleHQsIHN0ciksIHJlcHIodGV4dCkKICAgIHJldHVybiBsaXN0X3RvX3N0YWNrKHRl
eHQuc3BsaXRsaW5lcygpKSwgc3RhY2sKCgpAaW5zdGFsbApAU2ltcGxlRnVuY3Rpb25XcmFwcGVy
CmRlZiBoaXlhKHN0YWNrKToKICAgIGlmIGQuZm9jdXNlZF92aWV3ZXI6CiAgICAgICAgZC5mb2N1
c2VkX3ZpZXdlci5pbnNlcnQoJ0hpIFdvcmxkIScpCiAgICByZXR1cm4gc3RhY2sKUEsDBBQAAAAA
AIhkd0xJJ94ZORAAADkQAAALAAAAc2NyYXRjaC50eHRXaGF0IGlzIGl0PwoKQSBzaW1wbGUgR3Jh
cGhpY2FsIFVzZXIgSW50ZXJmYWNlIGZvciB0aGUgSm95IHByb2dyYW1taW5nIGxhbmd1YWdlLAp3
cml0dGVuIHVzaW5nIFB5Z2FtZSB0byBieXBhc3MgWDExIGV0LiBhbC4sIG1vZGVsZWQgb24gdGhl
IE9iZXJvbiBPUywgYW5kCmludGVuZGVkIHRvIGJlIGp1c3QgZnVuY3Rpb25hbCBlbm91Z2ggdG8g
c3VwcG9ydCBib290c3RyYXBwaW5nIGZ1cnRoZXIgSm95CmRldmVsb3BtZW50LgoKSXQncyBiYXNp
YyBmdW5jdGlvbmFsaXR5IGlzIG1vcmUtb3ItbGVzcyBhcyBhIGNydWRlIHRleHQgZWRpdG9yIGFs
b25nIHdpdGgKYSBzaW1wbGUgSm95IHJ1bnRpbWUgKGludGVycHJldGVyLCBzdGFjaywgYW5kIGRp
Y3Rpb25hcnkuKSAgSXQgYXV0by0gc2F2ZXMKYW55IG5hbWVkIGZpbGVzIChpbiBhIHZlcnNpb25l
ZCBob21lIGRpcmVjdG9yeSkgYW5kIHlvdSBjYW4gd3JpdGUgbmV3IEpveQpwcmltaXRpdmVzIGlu
IFB5dGhvbiBhbmQgSm95IGRlZmluaXRpb25zIGFuZCBpbW1lZGlhdGVseSBpbnN0YWxsIGFuZCB1
c2UKdGhlbSwgYXMgd2VsbCBhcyByZWNvcmRpbmcgdGhlbSBmb3IgcmV1c2UgKGFmdGVyIHJlc3Rh
cnRzLikKCkN1cnJlbnRseSwgdGhlcmUgYXJlIG9ubHkgdHdvIGtpbmRzIG9mIChpbnRlcmVzdGlu
Zykgdmlld2VyczogVGV4dFZpZXdlcnMKYW5kIFN0YWNrVmlld2VyLiBUaGUgVGV4dFZpZXdlcnMg
YXJlIGNydWRlIHRleHQgZWRpdG9ycy4gIFRoZXkgcHJvdmlkZQpqdXN0IGVub3VnaCBmdW5jdGlv
bmFsaXR5IHRvIGxldCB0aGUgdXNlciB3cml0ZSB0ZXh0IGFuZCBjb2RlIChQeXRob24gYW5kCkpv
eSkgYW5kIGV4ZWN1dGUgSm95IGZ1bmN0aW9ucy4gIE9uZSBpbXBvcnRhbnQgdGhpbmcgdGhleSBk
byBpcwphdXRvbWF0aWNhbGx5IHNhdmUgdGhlaXIgY29udGVudCBhZnRlciBjaGFuZ2VzLiAgTm8g
bW9yZSBsb3N0IHdvcmsuCgpUaGUgU3RhY2tWaWV3ZXIgaXMgYSBzcGVjaWFsaXplZCBUZXh0Vmll
d2VyIHRoYXQgc2hvd3MgdGhlIGNvbnRlbnRzIG9mIHRoZQpKb3kgc3RhY2sgb25lIGxpbmUgcGVy
IHN0YWNrIGl0ZW0uICBJdCdzIGEgdmVyeSBoYW5keSB2aXN1YWwgYWlkIHRvIGtlZXAKdHJhY2sg
b2Ygd2hhdCdzIGdvaW5nIG9uLiAgVGhlcmUncyBhbHNvIGEgbG9nLnR4dCBmaWxlIHRoYXQgZ2V0
cyB3cml0dGVuCnRvIHdoZW4gY29tbWFuZHMgYXJlIGV4ZWN1dGVkLCBhbmQgc28gcmVjb3JkcyB0
aGUgbG9nIG9mIHVzZXIgYWN0aW9ucyBhbmQKc3lzdGVtIGV2ZW50cy4gIEl0IHRlbmRzIHRvIGZp
bGwgdXAgcXVpY2tseSBzbyB0aGVyZSdzIGEgcmVzZXRfbG9nIGNvbW1hbmQKdGhhdCBjbGVhcnMg
aXQgb3V0LgoKVmlld2VycyBoYXZlICJncm93IiBhbmQgImNsb3NlIiBpbiB0aGVpciBtZW51IGJh
cnMuICBUaGVzZSBhcmUgYnV0dG9ucy4KV2hlbiB5b3UgcmlnaHQtY2xpY2sgb24gZ3JvdyBhIHZp
ZXdlciBhIGNvcHkgaXMgY3JlYXRlZCB0aGF0IGNvdmVycyB0aGF0CnZpZXdlcidzIGVudGlyZSB0
cmFjay4gIElmIHlvdSBncm93IGEgdmlld2VyIHRoYXQgYWxyZWFkeSB0YWtlcyB1cCBpdHMKd2hv
bGUgdHJhY2sgdGhlbiBhIGNvcHkgaXMgY3JlYXRlZCB0aGF0IHRha2VzIHVwIGFuIGFkZGl0aW9u
YWwgdHJhY2ssIHVwCnRvIHRoZSB3aG9sZSBzY3JlZW4uICBDbG9zaW5nIGEgdmlld2VyIGp1c3Qg
ZGVsZXRlcyB0aGF0IHZpZXdlciwgYW5kIHdoZW4KYSB0cmFjayBoYXMgbm8gbW9yZSB2aWV3ZXJz
LCBpdCBpcyBkZWxldGVkIGFuZCB0aGF0IGV4cG9zZXMgYW55IHByZXZpb3VzCnRyYWNrcyBhbmQg
dmlld2VycyB0aGF0IHdlcmUgaGlkZGVuLgoKKE5vdGU6IGlmIHlvdSBldmVyIGNsb3NlIGFsbCB0
aGUgdmlld2VycyBhbmQgYXJlIHNpdHRpbmcgYXQgYSBibGFuayBzY3JlZW4Kd2l0aCAgbm93aGVy
ZSB0byB0eXBlIGFuZCBleGVjdXRlIGNvbW1hbmRzLCBwcmVzcyB0aGUgUGF1c2UvQnJlYWsga2V5
LgpUaGlzIHdpbGwgb3BlbiBhIG5ldyAidHJhcCIgdmlld2VyIHdoaWNoIHlvdSBjYW4gdGhlbiB1
c2UgdG8gcmVjb3Zlci4pCgpDb3BpZXMgb2YgYSB2aWV3ZXIgYWxsIHNoYXJlIHRoZSBzYW1lIG1v
ZGVsIGFuZCB1cGRhdGUgdGhlaXIgZGlzcGxheSBhcyBpdApjaGFuZ2VzLiAoSWYgeW91IGhhdmUg
dHdvIHZpZXdlcnMgb3BlbiBvbiB0aGUgc2FtZSBuYW1lZCByZXNvdXJjZSBhbmQgZWRpdApvbmUg
eW91J2xsIHNlZSB0aGUgb3RoZXIgdXBkYXRlIGFzIHlvdSB0eXBlLikKClVJIEd1aWRlCgpsZWZ0
IG1vdXNlIHNldHMgY3Vyc29yIGluIHRleHQsIGluIG1lbnUgYmFyIHJlc2l6ZXMgdmlld2VyIGlu
dGVyYWN0aXZlbHkKKHRoaXMgaXMgYSBsaXR0bGUgYnVnZ3kgaW4gdGhhdCB5b3UgY2FuIG1vdmUg
dGhlIG1vdXNlIHF1aWNrbHkgYW5kIGdldApvdXRzaWRlIHRoZSBtZW51LCBsZWF2aW5nIHRoZSB2
aWV3ZXIgaW4gdGhlICJyZXNpemluZyIgc3RhdGUuIFVudGlsIEkgZml4CnRoaXMsIHRoZSB3b3Jr
YXJvdW5kIGlzIHRvIGp1c3QgZ3JhYiB0aGUgbWVudSBiYXIgYWdhaW4gYW5kIHdpZ2dsZSBpdCBh
CmZldyBwaXhlbHMgYW5kIGxldCBnby4gIFRoaXMgd2lsbCByZXNldCB0aGUgbWFjaGluZXJ5LikK
ClJpZ2h0IG1vdXNlIGV4ZWN1dGVzIEpveSBjb21tYW5kIChmdW5jdGlvbnMpLCBhbmQgeW91IGNh
biBkcmFnIHdpdGggdGhlCnJpZ2h0IGJ1dHRvbiB0byBoaWdobGlnaHQgKHdlbGwsIHVuZGVybGlu
ZSkgY29tbWFuZHMuICBXb3JkcyB0aGF0IGFyZW4ndApuYW1lcyBvZiBKb3kgY29tbWFuZHMgd29u
J3QgYmUgdW5kZXJsaW5lZC4gIFJlbGVhc2UgdGhlIGJ1dHRvbiB0byBleGVjdXRlCnRoZSBjb21t
YW5kLgoKVGhlIG1pZGRsZSBtb3VzZSBidXR0b24gKHVzdWFsbHkgYSB3aGVlbCB0aGVzZSBkYXlz
KSBzY3JvbGxzIHRoZSB0ZXh0IGJ1dAp5b3UgY2FuIGFsc28gY2xpY2sgYW5kIGRyYWcgYW55IHZp
ZXdlciB3aXRoIGl0IHRvIG1vdmUgdGhhdCB2aWV3ZXIgdG8KYW5vdGhlciB0cmFjayBvciB0byBh
IGRpZmZlcmVudCBsb2NhdGlvbiBpbiB0aGUgc2FtZSB0cmFjay4gIFRoZXJlJ3Mgbm8KZGlyZWN0
IHZpc3VhbCBmZWVkYmFjayBmb3IgdGhpcyAoeWV0KSBidXQgdGhhdCBkb3Nlbid0IHNlZW0gdG8g
aW1wYWlyIGl0cwp1c2VmdWxuZXNzLgoKRjEsIEYyIC0gc2V0IHNlbGVjdGlvbiBiZWdpbiBhbmQg
ZW5kIG1hcmtlcnMgKGNydWRlIGJ1dCB1c2FibGUuKQoKRjMgLSBjb3B5IHNlbGVjdGVkIHRleHQg
dG8gdGhlIHRvcCBvZiB0aGUgc3RhY2suCgpTaGlmdC1GMyAtIGFzIGNvcHkgdGhlbiBydW4gInBh
cnNlIiBjb21tYW5kIG9uIHRoZSBzdHJpbmcuCgpGNCAtIGN1dCBzZWxlY3RlZCB0ZXh0IHRvIHRo
ZSB0b3Agb2YgdGhlIHN0YWNrLgoKU2hpZnQtRjQgLSBhcyBjdXQgdGhlbiBydW4gInBvcCIgKGRl
bGV0ZSBzZWxlY3Rpb24uKQoKSm95CgpQcmV0dHkgbXVjaCBhbGwgb2YgdGhlIHJlc3Qgb2YgdGhl
IGZ1bmN0aW9uYWxpdHkgb2YgdGhlIHN5c3RlbSBpcyBwcm92aWRlZApieSBleGVjdXRpbmcgSm95
IGNvbW1hbmRzIChha2EgZnVuY3Rpb25zLCBha2EgIndvcmRzIiBpbiBGb3J0aCkgYnkgcmlnaHQt
CmNsaWNraW5nIG9uIHRoZWlyIG5hbWVzIGluIGFueSB0ZXh0LgoKVG8gZ2V0IGhlbHAgb24gYSBK
b3kgZnVuY3Rpb24gc2VsZWN0IHRoZSBuYW1lIG9mIHRoZSBmdW5jdGlvbiBpbiBhClRleHRWaWV3
ZXIgdXNpbmcgRjEgYW5kIEYyLCB0aGVuIHByZXNzIHNoaWZ0LUYzIHRvIHBhcnNlIHRoZSBzZWxl
Y3Rpb24uClRoZSBmdW5jdGlvbiAocmVhbGx5IGl0cyBTeW1ib2wpIHdpbGwgYXBwZWFyIG9uIHRo
ZSBzdGFjayBpbiBicmFja2V0cyAoYQoicXVvdGVkIHByb2dyYW0iIHN1Y2ggYXMgIltwb3BdIi4p
ICBUaGVuIHJpZ2h0LWNsaWNrIG9uIHRoZSB3b3JkIGhlbHAgaW4KYW55IFRleHRWaWV3ZXIgKGlm
IGl0J3Mgbm90IGFscmVhZHkgdGhlcmUsIGp1c3QgdHlwZSBpdCBpbiBzb21ld2hlcmUuKQpUaGlz
IHdpbGwgcHJpbnQgdGhlIGRvY3N0cmluZyBvciBkZWZpbml0aW9uIG9mIHRoZSB3b3JkIChmdW5j
dGlvbikgdG8Kc3Rkb3V0LiAgQXQgc29tZSBwb2ludCBJJ2xsIHdyaXRlIGEgdGhpbmcgdG8gc2Vu
ZCB0aGF0IHRvIHRoZSBsb2cudHh0IGZpbGUKaW5zdGVhZCwgYnV0IGZvciBub3cgbG9vayBmb3Ig
b3V0cHV0IGluIHRoZSB0ZXJtaW5hbC4KUEsDBBQAAAAAACdbd0yW6MvDbQMAAG0DAAAPAAAAZGVm
aW5pdGlvbnMudHh0c2VlX3N0YWNrID09IGdvb2Rfdmlld2VyX2xvY2F0aW9uIG9wZW5fc3RhY2sK
c2VlX3Jlc291cmNlcyA9PSBsaXN0X3Jlc291cmNlcyBnb29kX3ZpZXdlcl9sb2NhdGlvbiBvcGVu
X3ZpZXdlcgpvcGVuX3Jlc291cmNlX2F0X2dvb2RfbG9jYXRpb24gPT0gZ29vZF92aWV3ZXJfbG9j
YXRpb24gb3Blbl9yZXNvdXJjZQpzZWVfbG9nID09ICJsb2cudHh0IiBvcGVuX3Jlc291cmNlX2F0
X2dvb2RfbG9jYXRpb24Kc2VlX2RlZmluaXRpb25zID09ICJkZWZpbml0aW9ucy50eHQiIG9wZW5f
cmVzb3VyY2VfYXRfZ29vZF9sb2NhdGlvbgpyb3VuZF90b19jZW50cyA9PSAxMDAgKiArKyBmbG9v
ciAxMDAgLwpyZXNldF9sb2cgPT0gImRlbCBsb2cubGluZXNbMTpdIDsgbG9nLmF0X2xpbmUgPSAw
IiBldmFsdWF0ZQpzZWVfbWVudSA9PSAibWVudS50eHQiIGdvb2Rfdmlld2VyX2xvY2F0aW9uIG9w
ZW5fcmVzb3VyY2UKCiMgT3JkZXJlZCBCaW5hcnkgVHJlZSBkYXRhc3RydWN0dXJlIGZ1bmN0aW9u
cy4KQlRyZWUtbmV3ID09IHN3YXAgW1tdIFtdXSBjb25zIGNvbnMKIF9CVHJlZS1QID09IG92ZXIg
W3BvcG9wIHBvcG9wIGZpcnN0XSBudWxsYXJ5CiBfQlRyZWUtVD4gPT0gW2NvbnMgY29ucyBkaXBk
ZF0gY29ucyBjb25zIGNvbnMgaW5mcmEKIF9CVHJlZS1UPCA9PSBbY29ucyBjb25zIGRpcGRdIGNv
bnMgY29ucyBjb25zIGluZnJhCiBfQlRyZWUtRSA9PSBwb3Agc3dhcCByb2xsPCByZXN0IHJlc3Qg
Y29ucyBjb25zCiBfQlRyZWUtcmVjdXIgPT0gX0JUcmVlLVAgW19CVHJlZS1UPl0gW19CVHJlZS1F
XSBbX0JUcmVlLVQ8XSBjbXAKQlRyZWUtYWRkID09IFtwb3BvcCBub3RdIFtbcG9wXSBkaXBkIEJU
cmVlLW5ld10gW10gW19CVHJlZS1yZWN1cl0gZ2VucmVjClBLAwQUAAAAAAAnW3dM2ibqo88EAADP
BAAACAAAAG1lbnUudHh0ICBuYW1lX3ZpZXdlcgogIGxpc3RfcmVzb3VyY2VzCiAgb3Blbl9yZXNv
dXJjZV9hdF9nb29kX2xvY2F0aW9uCiAgZ29vZF92aWV3ZXJfbG9jYXRpb24KICBvcGVuX3ZpZXdl
cgogIHNlZV9zdGFjawogIHNlZV9yZXNvdXJjZXMKICBzZWVfZGVmaW5pdGlvbnMKICBzZWVfbG9n
CiAgcmVzZXRfbG9nCgogIGluc2NyaWJlCiAgZXZhbHVhdGUKCiAgcG9wIGNsZWFyICAgIGR1cCBz
d2FwCgogIGFkZCBzdWIgbXVsIGRpdiB0cnVlZGl2IG1vZHVsdXMgZGl2bW9kCiAgcG0gKysgLS0g
c3VtIHByb2R1Y3QgcG93IHNxciBzcXJ0CiAgPCA8PSA9ID49ID4gPD4KICAmIDw8ID4+CgogIGkg
ZHVwZGlwCgohPSAlICYgKiAqZnJhY3Rpb24gKmZyYWN0aW9uMCArICsrIC0gLS0gLyA8IDw8IDw9
IDw+ID0gPiA+PSA+PiA/IF4KYWJzIGFkZCBhbmFtb3JwaGlzbSBhbmQgYXBwMSBhcHAyIGFwcDMg
YXQgYXZlcmFnZQpiIGJpbmFyeSBicmFuY2gKY2hvaWNlIGNsZWFyIGNsZWF2ZSBjb25jYXQgY29u
cwpkaW5mcmlyc3QgZGlwIGRpcGQgZGlwZGQgZGlzZW5zdGFja2VuIGRpdiBkaXZtb2QgZG93bl90
b196ZXJvIGRyb3AKZHVkaXBkIGR1cCBkdXBkIGR1cGRpcAplbnN0YWNrZW4gZXEKZmlyc3QgZmxh
dHRlbiBmbG9vciBmbG9vcmRpdgpnY2QgZ2UgZ2VucmVjIGdldGl0ZW0gZ3JhbmRfcmVzZXQgZ3QK
aGVscAppIGlkIGlmdGUgaW5mcmEgaW5zY3JpYmUKa2V5X2JpbmRpbmdzCmxlIGxlYXN0X2ZyYWN0
aW9uIGxvb3AgbHNoaWZ0IGx0Cm1hcCBtYXggbWluIG1vZCBtb2R1bHVzIG1vdXNlX2JpbmRpbmdz
IG11bApuZSBuZWcgbm90IG51bGxhcnkKb2Ygb3Igb3ZlcgpwYW0gcGFyc2UgcGljayBwbSBwb3Ag
cG9wZCBwb3BkZCBwb3BvcCBwb3cgcHJlZCBwcmltcmVjIHByb2R1Y3QKcXVvdGVkCnJhbmdlIHJh
bmdlX3RvX3plcm8gcmVtIHJlbWFpbmRlciByZW1vdmUgcmVzZXRfbG9nIHJlc3QgcmV2ZXJzZQpy
b2xsPCByb2xsPiByb2xsZG93biByb2xsdXAgcnNoaWZ0IHJ1bgpzZWNvbmQgc2VsZWN0IHNoYXJp
bmcgc2hvd19sb2cgc2h1bnQgc2l6ZSBzb3J0IHNxciBzcXJ0IHN0YWNrIHN0ZXAKc3RlcF96ZXJv
IHN1YiBzdWNjIHN1bSBzd2FhY2sgc3dhcCBzd29uY2F0IHN3b25zCnRha2UgdGVybmFyeSB0aGly
ZCB0aW1lcyB0cnVlZGl2IHRydXRoeSB0dWNrCnVuYXJ5IHVuY29ucyB1bmlxdWUgdW5pdCB1bnF1
b3RlZCB1bnN0YWNrCnZvaWQKd2FycmFudHkgd2hpbGUgd29yZHMKeCB4b3IKemlwClBLAQIUAxQA
AAAAACdbd0wAAAAAAAAAAAAAAAAHAAAAAAAAAAAAAACAgQAAAABsb2cudHh0UEsBAhQDFAAAAAAA
J1t3THd/ml4DAAAAAwAAAAwAAAAAAAAAAAAAAICBJQAAAHN0YWNrLnBpY2tsZVBLAQIUAxQAAAAA
ACpgd0yZVJ2HZAYAAGQGAAAKAAAAAAAAAAAAAACkgVIAAABsaWJyYXJ5LnB5UEsBAhQDFAAAAAAA
iGR3TEkn3hk5EAAAORAAAAsAAAAAAAAAAAAAAICB3gYAAHNjcmF0Y2gudHh0UEsBAhQDFAAAAAAA
J1t3TJboy8NtAwAAbQMAAA8AAAAAAAAAAAAAAICBQBcAAGRlZmluaXRpb25zLnR4dFBLAQIUAxQA
AAAAACdbd0zaJuqjzwQAAM8EAAAIAAAAAAAAAAAAAACAgdoaAABtZW51LnR4dFBLBQYAAAAABgAG
AFMBAADPHwAAAAA=''')))


if __name__ == '__main__':
    print create_data()